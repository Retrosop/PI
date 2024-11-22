unit Unit5;

interface

uses
  Windows, Messages, SysUtils, Variants, Classes, Graphics, Controls, Forms,
  Dialogs, StdCtrls, ExtCtrls, DBCtrls, DB, mySQLDbTables, Grids, DBGrids;

type
  TForm5 = class(TForm)
    Button1: TButton;
    DBGrid1: TDBGrid;
    MySQLTable1: TMySQLTable;
    MySQLDatabase1: TMySQLDatabase;
    DataSource1: TDataSource;
    DBNavigator1: TDBNavigator;
    Button2: TButton;
    procedure Button1Click(Sender: TObject);
    procedure Button2Click(Sender: TObject);
  private
    { Private declarations }
  public
    { Public declarations }
  end;

var
  Form5: TForm5;

implementation

uses Unit6;

{$R *.dfm}

procedure TForm5.Button1Click(Sender: TObject);
begin
 Form5.Close;
end;

procedure TForm5.Button2Click(Sender: TObject);
begin
form6.frxReport1.ShowReport
end;

end.
