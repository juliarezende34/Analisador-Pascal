program WhileAninhado;

var
    i, j: integer;

begin
    i := 1;

    writeln('Contagem com while aninhado:');
    writeln('-----------------------------');

    while i <= 3 do
    begin
        j := 1;
        while j <= 4 do
        begin
            writeln('i = ', i, ', j = ', j);
            j := j + 1;
        end;
        writeln('Fim do bloco de i = ', i);
        writeln('-----------------------------');
        i := i + 1;
    end;

end.
