program TesteCompleto;

var
    a, b: integer;
    x, y: real;
    resmod: real;
    resdiv: real;
    s: string;
    h: integer;
    o: integer;

begin
    { Entrada }

    a := a + 0xF;
    writeln(a)

    { For com bloco (múltiplas instruções) }
    for i := 1 to 3 do
    begin
        writeln('Número: ', i);
    end;

    { While }
    o := 0;
    while o < 2 do
    begin
        writeln('While: ', o);
        o := o + 1;
    end;

    { Strings }
    writeln('String: ', s);

end.
