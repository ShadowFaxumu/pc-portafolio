# Copyright (c) 28/10/2021
# Created by Paulina y Sáyago

function Use-UrlNmap($url) {
    $nmap2 = nmap.exe $url
    Write-Output "-----------------------------------------------------------"
    Write-Output "`n" "An nmap was performed to "$url $nmap2
}

#Results are saved without coding
$str = $args[0]
Use-UrlNmap($str) | Out-File -FilePath ./resultados.txt -Append