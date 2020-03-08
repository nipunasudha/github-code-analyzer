import csv


class DataList(object):
    user_dict = {}
    user_csv_path = 'csv/dataset_edit.csv'
    def __init__(self):
        # users
        user_id_list = []
        with open(self.user_csv_path, encoding="utf8") as f:
            users_array = [{k: v for k, v in row.items()}
                           for row in csv.DictReader(f, skipinitialspace=True)]
        for row in users_array:
            user_id = row['username']
            user_id_list.append(user_id)

            self.user_dict[user_id] = {'users': row}
    key_list = user_dict.keys()
    users_dict = []

    def get_user_data(self, i, count):
        user_features = {}
        user_data = self.user_dict[i]
        if count < 101:

            evaluator1 = (user_data['users']['user1'])
            evaluator2 = (user_data['users']['user2'])
            evaluator3 = (user_data['users']['user3'])

            round_mean_levl = (float(evaluator1) + float(evaluator2) + float(evaluator3)) / 3
            print(round_mean_levl)
            if 1.8 >= round_mean_levl >= 1:
                label = 'beginner'
            elif 2.9 >= round_mean_levl > 1.8:
                label = 'intermediate'
            elif 3 >= round_mean_levl > 2.9:
                label = 'advance'
            elif 4 >= round_mean_levl > 3:
                label = 'expert'
        self.id_and_label_list = []
        user_id = user_data["users"]["username"]
        self.id_and_label_list.append(user_id)
        self.id_and_label_list.append(label)

        user_features['languages'] = user_data["users"]["languages"]
        user_features['repo_count'] = user_data["users"]["repo_count"]
        user_features['total_commits'] = user_data["users"]["total_commits"]
        user_features['ins_best_practices'] = user_data["users"]["ins_best_practices"]
        user_features['ins_code_style'] = user_data["users"]["ins_code_style"]
        user_features['ins_design'] = user_data["users"]["ins_design"]
        user_features['ins_documentation'] = user_data["users"]["ins_documentation"]
        user_features['ins_error_prone'] = user_data["users"]["ins_error_prone"]
        user_features['ins_multithreading'] = user_data["users"]["ins_multithreading"]
        user_features['ins_performance'] = user_data["users"]["ins_performance"]
        user_features['ins_security'] = user_data["users"]["ins_security"]
        print(user_data)
        print(label)
        return user_features

    def get_feature_set_with_lable(self):
        s = 0
        for i in self.key_list:
            s = s + 1
            all_features_dict = self.get_user_data(i, s)
            all_features_dict["Id"] = self.id_and_label_list[0]
            all_features_dict["label"] = self.id_and_label_list[1]

            self.users_dict.append(all_features_dict)

        return self.users_dict


data = DataList()
list_data = data.get_feature_set_with_lable()


# print(list_data)

def normalize_all(data_list):
    keys_to_normalize = ['languages', 'repo_count', 'total_commits', 'ins_best_practices', 'ins_code_style',
                         'ins_design', 'ins_documentation', 'ins_error_prone',
                         'ins_multithreading', 'ins_performance', 'ins_security']
    max_dict = {}
    min_dict = {}
    i = 2000
    threshold_max = 10000
    for row in data_list:
        for key in keys_to_normalize:
            if key not in max_dict:
                max_dict[key] = 0
            if key not in min_dict:
                min_dict[key] = 99999
            max_dict[key] = min(max(max_dict[key], int(row[key])), threshold_max)
            min_dict[key] = min(min_dict[key], int(row[key]))

    # print(max_dict)
    for row in data_list:
        for key in keys_to_normalize:
            ori_val = int(row[key])
            diff = (max_dict[key] - min_dict[key])
            if diff == 0:
                row[key] = 0
                continue
            norm_val = (min(ori_val, threshold_max) - min_dict[key]) / diff
            row[key] = norm_val
        # print(row)
    pass


normalize_all(list_data)

keys = list_data[0].keys()

with open('./generated_csv/direct_features.csv', 'w', newline='') as output_file:
    dict_writer = csv.DictWriter(output_file, keys)
    dict_writer.writeheader()
    dict_writer.writerows(list_data[:35])

with open('./generated_csv/direct_predict.csv', 'w', newline='') as output_file:
    dict_writer = csv.DictWriter(output_file, keys)
    dict_writer.writeheader()
    dict_writer.writerows(list_data[35:])
