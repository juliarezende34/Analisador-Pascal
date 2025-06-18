program float;
var
  x: integer; 

begin
  for i := 1 to 10 do
    begin
      writeln('Número: ', i);
      x := x * 1.1;
  end;
end.