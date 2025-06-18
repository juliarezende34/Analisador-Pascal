program teste;
var
    i: integer;
    x: real;
begin
    i := 0;
    x := 3.14;

    { If sem begin/end (1 instrução) }
    if (x >= 0) then
    begin
        writeln('x é positivo');
    end;

    { For com bloco (múltiplas instruções) }
    for i := 1 to 10 do
    begin
        writeln('Número: ', i);
        x := x * 1.1;
    end;
end.