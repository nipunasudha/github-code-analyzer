Requirements:

You need git on the computer for single cloning

run this in powershell on ADMINISTRATOR MODE

`
Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))
`

then install pmd
`choco install -y pmd`