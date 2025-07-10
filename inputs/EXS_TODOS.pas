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
    read(a);
    readln(b);
    read(x);
    readln(y);
    readln(s);

    { Atribuição }
    a := a + 1;
    b := b - 2;
    x := x * 2.5;
    y := y / 2.0;
    s := 'Teste';

    { Operadores relacionais }
    if a = b then
        writeln('a igual a b');
    else if a <> b then
        writeln('a diferente de b');
    else if x < y then
        writeln('x menor que y');
    else if x > y then
        writeln('x maior que y');
    else if x <= y then
        writeln('x menor ou igual a y');
    else if x >= y then
        writeln('x maior ou igual a y');
    else
        writeln('Fim dos testes relacionais');

    { Operadores lógicos }
    if (a > 0) and (b > 0) then
        writeln('a e b são positivos');
    if (x > 0) or (y > 0) then
        writeln('x ou y é positivo');
    if not (a = 0) then
        writeln('a não é zero');

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

    { Mod, Div }
    a := 10;
    b := 3;
    resmod := a mod b;
    resdiv := a div b;
    writeln('a mod b = ', resmod);
    writeln('a div b = ', resdiv);

    { Strings }
    writeln('String: ', s);

end.