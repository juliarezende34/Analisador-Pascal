program TesteModDivFora;

var
    a, b, res_mod, res_div: integer;

begin
    a := 10;
    b := 3;
    res_mod := a mod b;
    res_div := a div b;
    writeln('a mod b = ', res_mod);
    writeln('a div b = ', res_div);
end.
