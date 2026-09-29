$out="$PSScriptRoot\diag.txt"
$k=$env:AGNES_API_KEY; if ($k) { $k=$k.Trim() }
$f=(Get-Content "$PSScriptRoot\cle-agnes.txt" -Raw).Trim()
"$(Get-Date -Format HH:mm:ss) env present: $([bool]$k) egal fichier: $($k -eq $f)" | Set-Content $out
function T($nom,$cle,$uri,$meth,$body) {
  try {
    $p=@{Uri=$uri;Method=$meth;Headers=@{Authorization="Bearer $cle"};UseBasicParsing=$true}
    if ($body) { $p.ContentType="application/json; charset=utf-8"; $p.Body=[Text.Encoding]::UTF8.GetBytes($body) }
    $r=Invoke-WebRequest @p; "$nom -> $($r.StatusCode) $($r.Content.Substring(0,[math]::Min(200,$r.Content.Length)))" | Add-Content $out
  } catch { "$nom -> ERR $($_.Exception.Message) $($_.ErrorDetails.Message)" | Add-Content $out }
}
$b='{"model":"agnes-image-2.1-flash","prompt":"a red apple on a wooden table, photorealistic","size":"768x768","n":1}'
T "faux jeton /v1/models" "sk-faux" "https://apihub.agnes-ai.com/v1/models" "GET" $null
T "cle /v1/models" $f "https://apihub.agnes-ai.com/v1/models" "GET" $null
T "cle image" $f "https://apihub.agnes-ai.com/v1/images/generations" "POST" $b
T "cle solde" $f "https://apihub.agnes-ai.com/v1/dashboard/billing/subscription" "GET" $null
