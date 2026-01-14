param (
    [int]$Workers = 1
)

Write-Host "Starting $Workers workers..."

for ($i = 1; $i -le $Workers; $i++) {
    Start-Process powershell `
        -ArgumentList "-NoExit", "-Command", "cd '$PSScriptRoot'; python worker.py"
}
