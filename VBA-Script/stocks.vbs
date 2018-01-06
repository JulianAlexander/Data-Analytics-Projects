Sub sumStocks():

Dim rcount As Double
Dim ucount As Double
Dim lastrow As Double
Dim i As Double
Dim x As Double
Dim sumTotal As Double
Dim rtotal As Double
Dim WS_Count As Integer
Dim U As Integer
Dim ws As Worksheet
Dim starting_ws As Worksheet
Dim e As Double
Dim l As Double
Dim pchange As Double
Dim dchange As Double
Dim avgdchange As Double
Dim tchange As Double
Dim c As Long
Dim count2 As Double
Dim highchange As Variant
Dim lowchange As Variant

For Each ws In Worksheets

    With ws
        .Range("A:A").AdvancedFilter Action:=xlFilterCopy, CopyToRange:=.Range("K1"), Unique:=True 'creates list of unique ticker names
        rcount = .Range("A" & Rows.Count).End(xlUp).Row 'gives count of total rows in sheet
        ucount = .Range("K" & Rows.Count).End(xlUp).Row 'gives count of unique ticker names in sheet
        .Cells(1, 13) = rcount
        .Cells(1, 14) = ucount
        c = 0
    
        For x = 2 To ucount
            sumTotal = 0
            rtotal = 0
            dchange = 0
            pchange = 0
            tchange = 0
            count2 = WorksheetFunction.CountIf(.Range("A2:A43398"), .Cells(x, 11))
            .Cells(1, 12) = "Yearly Change"
            .Cells(1, 13) = "Percent Change"
            .Cells(1, 14) = "Total Volume"

                        
            For i = 2 To 262 'count2 'for loop which runs from i=2 through the total rcount

                
                If .Cells(i + c, 1).Value = .Cells(x, 11).Value Then
                    rtotal = rtotal + .Cells(i + c, 7).Value 'running total of ticker volume for each unique ticker
                    dchange = dchange + .Cells(i + c, 5).Value - Cells(i + c, 4).Value 'calculates daily change high minus low
                'Else
                    If .Cells(i + c, 2).Value Like ("*0101") Or .Cells(i + c, 2).Value Like ("*0102") Then 'Or .Cells(i + c, 2).Value = 20140101 Then
                        e = .Cells(i + c, 6).Value 'assigns e to the earliest closing value for ticker
                    End If
                    If .Cells(i + c, 2).Value Like ("*123*") Then ' latedate Then
                        l = .Cells(i + c, 6).Value 'assigns l to the last closing value for ticker
                    End If
                End If
                

                
                
            Next i
            c = c + count2
            .Cells(x, 17) = c
            .Cells(x, 14).Value = rtotal
            tchange = e - l 'calculates the total change of the stock over the year
            .Cells(x, 12).Value = tchange
            If tchange > 0 Then
                .Cells(x, 12).Interior.ColorIndex = 4
            ElseIf tchange < 0 Then
                .Cells(x, 12).Interior.ColorIndex = 3
            End If
            pchange = (tchange / e)

                      
        Next x

    'Next U
    End With

Next ws
End Sub

