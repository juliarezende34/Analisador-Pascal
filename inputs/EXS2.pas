program exemplo2;

var
    x: integer;
    y: integer;

begin
    read(x);
    read(y);

    if (x > y) and (y <> 0) then
        writeln('X é maior e Y não é zero');
    else
        write('Condição falsa');
end.
