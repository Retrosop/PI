object Form2: TForm2
  Left = 220
  Top = 1027
  Width = 745
  Height = 557
  Caption = 'Klienti'
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
    Left = 8
    Top = 416
    Width = 75
    Height = 25
    Caption = 'Button1'
    TabOrder = 0
    OnClick = Button1Click
  end
  object DBGrid1: TDBGrid
    Left = 8
    Top = 8
    Width = 585
    Height = 137
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
        FieldName = 'pultovii_nomer'
        Visible = True
      end
      item
        Expanded = False
        FieldName = 'adres'
        Visible = True
      end
      item
        Expanded = False
        FieldName = 'pribor'
        Visible = True
      end
      item
        Expanded = False
        FieldName = 'kil-vo shleif'
        Visible = True
      end
      item
        Expanded = False
        FieldName = 'data podklucheniya'
        Visible = True
      end
      item
        Expanded = False
        FieldName = 'prikaz'
        Visible = True
      end>
  end
  object DBNavigator1: TDBNavigator
    Left = 8
    Top = 144
    Width = 580
    Height = 25
    DataSource = DataSource1
    TabOrder = 2
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
    Left = 624
    Top = 8
  end
  object MySQLTable1: TMySQLTable
    Database = MySQLDatabase1
    Active = True
    TableName = 'Eremenko_klienti'
    Left = 624
    Top = 80
  end
  object DataSource1: TDataSource
    DataSet = MySQLTable1
    Left = 624
    Top = 48
  end
end
