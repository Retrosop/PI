object Form6: TForm6
  Left = 417
  Top = 274
  Width = 724
  Height = 658
  Caption = 'Form6'
  Color = clBtnFace
  Enabled = False
  Font.Charset = DEFAULT_CHARSET
  Font.Color = clWindowText
  Font.Height = -11
  Font.Name = 'MS Sans Serif'
  Font.Style = []
  OldCreateOrder = False
  PixelsPerInch = 96
  TextHeight = 13
  object frxPreview1: TfrxPreview
    Left = 0
    Top = 0
    Width = 569
    Height = 609
    OutlineVisible = True
  end
  object frxReport1: TfrxReport
    DataSet = frxDBDataset1
    DataSetName = 'frxDBDataset1'
    DotMatrixReport = False
    IniFile = '\Software\Fast Reports'
    PreviewOptions.Buttons = [pbPrint, pbLoad, pbSave, pbExport, pbZoom, pbFind, pbOutline, pbPageSetup, pbTools, pbEdit, pbNavigator]
    PreviewOptions.Zoom = 1.000000000000000000
    PrintOptions.Printer = 'Default'
    ReportOptions.CreateDate = 45618.506243854160000000
    ReportOptions.LastChange = 45618.520876319450000000
    ScriptLanguage = 'PascalScript'
    ScriptText.Strings = (
      'begin'
      ''
      'end.')
    Left = 576
    Top = 40
    Datasets = <
      item
        DataSet = frxDBDataset1
        DataSetName = 'frxDBDataset1'
      end>
    Variables = <>
    Style = <>
    object Page1: TfrxReportPage
      PaperWidth = 210.000000000000000000
      PaperHeight = 297.000000000000000000
      PaperSize = 9
      LeftMargin = 10.000000000000000000
      RightMargin = 10.000000000000000000
      TopMargin = 10.000000000000000000
      BottomMargin = 10.000000000000000000
      object Memo1: TfrxMemoView
        Left = -7.559060000000000000
        Top = 37.795300000000000000
        Width = 1198.111010000000000000
        Height = 22.677180000000000000
        DataField = 'pultovii_nomer'
        DataSet = frxDBDataset1
        DataSetName = 'frxDBDataset1'
        Memo.Strings = (
          '[frxDBDataset1."pultovii_nomer"]')
      end
      object Memo2: TfrxMemoView
        Left = 192.756030000000000000
        Top = 41.574830000000000000
        Width = 79.370130000000000000
        Height = 18.897650000000000000
        DataField = 'pribor'
        DataSet = frxDBDataset1
        DataSetName = 'frxDBDataset1'
        Memo.Strings = (
          '[frxDBDataset1."pribor"]')
      end
      object Memo3: TfrxMemoView
        Left = 355.275820000000000000
        Top = 41.574830000000000000
        Width = 79.370130000000000000
        Height = 18.897650000000000000
        DataField = 'adres'
        DataSet = frxDBDataset1
        DataSetName = 'frxDBDataset1'
        Memo.Strings = (
          '[frxDBDataset1."adres"]')
      end
      object Memo4: TfrxMemoView
        Left = 272.126160000000000000
        Top = 41.574830000000000000
        Width = 79.370130000000000000
        Height = 18.897650000000000000
        DataField = 'kil-vo shleif'
        DataSet = frxDBDataset1
        DataSetName = 'frxDBDataset1'
        Memo.Strings = (
          '[frxDBDataset1."kil-vo shleif"]')
      end
      object Memo5: TfrxMemoView
        Left = 442.205010000000000000
        Top = 41.574830000000000000
        Width = 79.370130000000000000
        Height = 18.897650000000000000
        DataField = 'data podklucheniya'
        DataSet = frxDBDataset1
        DataSetName = 'frxDBDataset1'
        Memo.Strings = (
          '[frxDBDataset1."data podklucheniya"]')
      end
      object Memo6: TfrxMemoView
        Left = 525.354670000000000000
        Top = 41.574830000000000000
        Width = 1198.111010000000000000
        Height = 18.897650000000000000
        DataField = 'prikaz'
        DataSet = frxDBDataset1
        DataSetName = 'frxDBDataset1'
        Memo.Strings = (
          '[frxDBDataset1."prikaz"]')
      end
      object Memo7: TfrxMemoView
        Left = -7.559060000000000000
        Top = 64.252010000000000000
        Width = 1198.111010000000000000
        Height = 22.677180000000000000
        DataField = 'pultovii_nomer'
        DataSet = frxDBDataset1
        DataSetName = 'frxDBDataset1'
        Memo.Strings = (
          '[frxDBDataset1."pultovii_nomer"]')
      end
      object Memo8: TfrxMemoView
        Left = 192.756030000000000000
        Top = 68.031540000000000000
        Width = 79.370130000000000000
        Height = 18.897650000000000000
        DataField = 'pribor'
        DataSet = frxDBDataset1
        DataSetName = 'frxDBDataset1'
        Memo.Strings = (
          '[frxDBDataset1."pribor"]')
      end
      object Memo9: TfrxMemoView
        Left = 355.275820000000000000
        Top = 68.031540000000000000
        Width = 79.370130000000000000
        Height = 18.897650000000000000
        DataField = 'adres'
        DataSet = frxDBDataset1
        DataSetName = 'frxDBDataset1'
        Memo.Strings = (
          '[frxDBDataset1."adres"]')
      end
      object Memo10: TfrxMemoView
        Left = 272.126160000000000000
        Top = 68.031540000000000000
        Width = 79.370130000000000000
        Height = 18.897650000000000000
        DataField = 'kil-vo shleif'
        DataSet = frxDBDataset1
        DataSetName = 'frxDBDataset1'
        Memo.Strings = (
          '[frxDBDataset1."kil-vo shleif"]')
      end
      object Memo11: TfrxMemoView
        Left = 442.205010000000000000
        Top = 68.031540000000000000
        Width = 79.370130000000000000
        Height = 18.897650000000000000
        DataField = 'data podklucheniya'
        DataSet = frxDBDataset1
        DataSetName = 'frxDBDataset1'
        Memo.Strings = (
          '[frxDBDataset1."data podklucheniya"]')
      end
      object Memo12: TfrxMemoView
        Left = 525.354670000000000000
        Top = 68.031540000000000000
        Width = 1198.111010000000000000
        Height = 18.897650000000000000
        DataField = 'prikaz'
        DataSet = frxDBDataset1
        DataSetName = 'frxDBDataset1'
        Memo.Strings = (
          '[frxDBDataset1."prikaz"]')
      end
    end
    object Page2: TfrxReportPage
      PaperWidth = 210.000000000000000000
      PaperHeight = 297.000000000000000000
      PaperSize = 9
      LeftMargin = 10.000000000000000000
      RightMargin = 10.000000000000000000
      TopMargin = 10.000000000000000000
      BottomMargin = 10.000000000000000000
    end
  end
  object frxDBDataset1: TfrxDBDataset
    UserName = 'frxDBDataset1'
    CloseDataSource = False
    FieldAliases.Strings = (
      '-id_klienta=id_klienta'
      'pultovii_nomer=pultovii_nomer'
      'adres=adres'
      'pribor=pribor'
      'kil-vo shleif=kil-vo shleif'
      'data podklucheniya=data podklucheniya'
      'prikaz=prikaz')
    DataSet = Form2.MySQLTable1
    Left = 576
    Top = 96
  end
end
