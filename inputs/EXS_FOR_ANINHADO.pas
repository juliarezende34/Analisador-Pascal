program ForAninhado;

var
    i, j, resultado: integer;

begin
    writeln('Tabela de Multiplicação de 1 a 5:');
    writeln('----------------------------------');

    for i := 1 to 5 do
    begin
        for j := 1 to 5 do
        begin
            resultado := i * j;
            writeln(i, ' x ', j, ' = ', resultado);
        end;
        writeln('--------------------------');
    end;

end.
