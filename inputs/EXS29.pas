program testeExpressoes;

var
  a, b, c: integer;
  x, y, z: real;

begin
  a := 10;
  b := 5;
  c := 2;
  
  x := 3.14;
  y := 2.5;
  z := 1.0;
  
  flag := true;
  
  { Expressões aritméticas básicas }
  a := a + b * c;
  z := (x + y) / z;
  
  { Expressões booleanas }
  flag := (a > b) and (x < y) or not flag;
  
  { Expressões em comandos de saída }
  writeln('Valor de a: ', a);
  writeln('Valor de z: ', z);
  writeln('Flag: ', flag);
  
  { Expressão condicional }
  if (x > 0) then
    begin
        writeln('Positivo');
        x := x + 1;
    end;
    else
    begin 
        writeln('Negativo');
        x := 0;
    end;
  
  { Loop com expressão }
  while (b < 20) and (y > 1.0) do
    begin
    b := b + 1;
    y := y - 0.1;
    end;
  
  writeln('Valor final de b: ', b);
  writeln('Valor final de y: ', y);
end.