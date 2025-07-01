program exemplo3;

var
    i: integer;
    soma: integer;

begin
    soma := 0;

    for i := 1 to 5 do
    begin
        if i == 3+2 then
            continue;
        soma := soma + i;
    end;  
    
    while soma < 20 do
    begin
        soma := soma + 2;
        if soma == 18 then
            break;
    end;

    writeln('Soma final: ', soma);
    
    
end.
