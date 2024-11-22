object Form5: TForm5
  Left = 466
  Top = 180
  Width = 1005
  Height = 731
  Caption = 'Form5'
  Color = clBtnFace
  Font.Charset = DEFAULT_CHARSET
  Font.Color = clWindowText
  Font.Height = -11
  Font.Name = 'MS Sans Serif'
  Font.Style = []
  OldCreateOrder = False
  PixelsPerInch = 96
  TextHeight = 13
  object Button1: TButton
    Left = 0
    Top = 368
    Width = 75
    Height = 25
    Caption = 'Button1'
    TabOrder = 0
    OnClick = Button1Click
  end
  object DBGrid1: TDBGrid
    Left = -8
    Top = 0
    Width = 585
    Height = 329
    DataSource = DataSource1
    TabOrder = 1
    TitleFont.Charset = DEFAULT_CHARSET
    TitleFont.Color = clWindowText
    TitleFont.Height = -11
    TitleFont.Name = 'MS Sans Serif'
    TitleFont.Style = []
    Columns = <
      item
        Expanded = False
        FieldName = 'Sistema'
        Width = 59
        Visible = True
      end
      item
        Expanded = False
        FieldName = 'pyltovii_nomer'
        Width = 78
        Visible = True
      end
      item
        Expanded = False
        FieldName = 'Data_srabotki'
        Visible = True
      end
      item
        Expanded = False
        FieldName = 'Vremya srabotki'
        Visible = True
      end
      item
        Expanded = False
        FieldName = 'Klient'
        Visible = True
      end
      item
        Expanded = False
        FieldName = 'Ekipaj'
        Visible = True
      end
      item
        Expanded = False
        FieldName = 'prichina'
        Visible = True
      end
      item
        Expanded = False
        FieldName = 'sotrydnik'
        Visible = True
      end>
  end
  object DBNavigator1: TDBNavigator
    Left = 0
    Top = 328
    Width = 570
    Height = 25
    DataSource = DataSource1
    TabOrder = 2
  end
  object Button2: TButton
    Left = 104
    Top = 376
    Width = 75
    Height = 25
    Caption = 'Otchet'
    TabOrder = 3
    OnClick = Button2Click
  end
  object MySQLTable1: TMySQLTable
    Database = MySQLDatabase1
    Active = True
    TableName = 'Eremenko_srabotka111'
    Left = 672
    Top = 176
  end
  object MySQLDatabase1: TMySQLDatabase
    Connected = True
    DatabaseName = 'bh35910_ais'
    UserName = 'bh35910_student1711'
    UserPassword = 'pgu2023pgu2023'
    Host = '91.219.194.4'
    ConnectOptions = []
    ConnectionCharacterSet = 'utf8'
    Params.Strings = (
      'Port=3306'
      'TIMEOUT=30'
      'DatabaseName=bh35910_ais'
      'UID=bh35910_student1711'
      'PWD=pgu2023pgu2023'
      'Host=91.219.194.4')
    DatasetOptions = []
    Left = 672
    Top = 136
  end
  object DataSource1: TDataSource
    DataSet = MySQLTable1
    Left = 752
    Top = 152
  end
end
