$counter = 1;
while (1) {
    $msg1 = [string]::Format("INFO this is goot {0}", $counter)
    Write-Output $msg1
    sleep 1
    $msg2 = [string]::Format("ERROR this is bat {0}", $counter)
    Write-Output $msg2
    sleep 1
    $counter++
}
