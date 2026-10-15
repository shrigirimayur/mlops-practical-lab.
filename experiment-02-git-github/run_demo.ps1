$ErrorActionPreference = "Stop"

$demo = Join-Path ([System.IO.Path]::GetTempPath()) (
    "mlops-git-practical-" + [guid]::NewGuid().ToString("N")
)
New-Item -ItemType Directory -Path $demo | Out-Null

function Invoke-DemoGit {
    param([string[]]$Arguments)

    & git -C $demo @Arguments
    if ($LASTEXITCODE -ne 0) {
        throw "Git command failed: git $($Arguments -join ' ')"
    }
}

try {
    Invoke-DemoGit @("init", "--quiet", "--initial-branch", "main")
    Invoke-DemoGit @("config", "user.name", "MLOps Practical")
    Invoke-DemoGit @("config", "user.email", "mlops-practical@example.invalid")

    Set-Content -LiteralPath (Join-Path $demo "notes.txt") `
        -Value "Project status: initial" -NoNewline
    Invoke-DemoGit @("add", "notes.txt")
    Invoke-DemoGit @("commit", "--quiet", "-m", "Add baseline")
    $baseline = (& git -C $demo rev-parse --short HEAD).Trim()

    Invoke-DemoGit @("switch", "--quiet", "-c", "feature/report")
    Set-Content -LiteralPath (Join-Path $demo "notes.txt") `
        -Value "Project status: feature report" -NoNewline
    Invoke-DemoGit @("commit", "--quiet", "-am", "Update on feature branch")
    $feature = (& git -C $demo rev-parse --short HEAD).Trim()

    Invoke-DemoGit @("switch", "--quiet", "main")
    Set-Content -LiteralPath (Join-Path $demo "notes.txt") `
        -Value "Project status: data pipeline" -NoNewline
    Invoke-DemoGit @("commit", "--quiet", "-am", "Update on main")
    $main = (& git -C $demo rev-parse --short HEAD).Trim()

    Write-Output "Temporary repository: isolated from the assignment repository"
    Write-Output "main: $baseline Add baseline"
    Write-Output "feature/report: $feature Update on feature branch"
    Write-Output "main: $main Update on main"

    $mergeOutput = & git -C $demo merge --no-edit feature/report 2>&1
    $mergeCode = $LASTEXITCODE
    $mergeOutput | ForEach-Object { Write-Output $_ }
    if ($mergeCode -ne 1) {
        throw "Expected a content conflict; git merge returned $mergeCode."
    }
    Write-Output "merge exit code: $mergeCode"

    Set-Content -LiteralPath (Join-Path $demo "notes.txt") `
        -Value "Project status: integrated report and data pipeline" -NoNewline
    Invoke-DemoGit @("add", "notes.txt")
    Invoke-DemoGit @("commit", "--quiet", "-m", "Resolve merge conflict")

    Write-Output "After resolving the conflict:"
    & git -C $demo log --oneline --graph -4
    if ($LASTEXITCODE -ne 0) {
        throw "Could not read the demonstration commit history."
    }
    Write-Output "Final repository status:"
    $status = (& git -C $demo status --short | Out-String).Trim()
    if ($LASTEXITCODE -ne 0) {
        throw "Could not read the demonstration repository status."
    }
    Write-Output $(if ($status) { $status } else { "clean on main" })
}
finally {
    if (Test-Path -LiteralPath $demo) {
        Remove-Item -LiteralPath $demo -Recurse -Force
    }
}
