program ExemploLEG;
var
    a: integer;
    b: real;
    c: string;
begin
    a := 5.5;
    b := 6;
    c := 'Lucas';
    if a == c then
        writeln('a é menor que b (LESS)');
    else if a = b then
        writeln('a é igual a b (LEG)');
    else
        writeln('a é maior que b (GEGA)');
end.
