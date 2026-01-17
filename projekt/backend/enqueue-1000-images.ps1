param (
    [int]$Count = 1000
)

$Url = "http://localhost:8000/count-people-from-local"

Write-Host "Sending $Count jobs to queue..."

1..$Count | ForEach-Object {
    Invoke-RestMethod -Uri $Url -Method GET | Out-Null
}
