Install-Module -Name ImportExcel -RequiredVersion 7.8.5
Import-Module ImportExcel
# 获取当前脚本的目录
$scriptDirectory = $PSScriptRoot

# Excel 文件相对路径
$excelFileName = "abc.xlsx"

# Excel 文件路径
$excelFilePath = Join-Path $scriptDirectory $excelFileName

# Sheet 名称
$sheetName = "abc"

# 读取 Excel 文件数据
$data = Import-Excel -Path $excelFilePath -WorksheetName $sheetName -HeaderName A,B,C

# 按照 A 列的第一部分和 B 列进行升序排列
$sortedData = $data | Sort-Object { $_.A -split ('-')[0] }, B

# Excel 输出路径
$resultExcelPath = Join-Path $scriptDirectory "result.xlsx"
 
# 导出到 Excel 文件
 
$sortedData | Export-Excel -Path $resultExcelPath -WorksheetName "result"  -AutoSize    -FreezeTopRow -BoldTopRow  
# 打印窗口
Start-Process $resultExcelPath #-Verb Print