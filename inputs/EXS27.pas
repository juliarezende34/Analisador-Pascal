program valoresMistos;
{ Programa com 8 valores float e 2 valores hexadecimais (formato 0x) }



const
  // Valores float
  PIvAL          := 3.14159265;
  EULERvAL       := 2.71828182;
  GRAVITY         := 9.80665;
  LIGHTsPEED     := 2.99792458e8;
  GOLDENrATIO    := 1.61803398;
  AVOGADRO        := 6.02214076e23;
  PLANCK          := 6.62607015e-34;
  ELECTRONcHARGE := 1.602176634e-19;

  // Valores hexadecimais (formato 0x)
  MASKfLAGS      := 0xFF00;
  ERRORcODE      := 0x1A3F;

var
  i: integer; 

begin
  clrscr;
  
  writeln('Demonstração de Valores Mistos');
  writeln('=============================');
  writeln;
  writeln('Valores Float Definidos:');
  writeln('------------------------');
  writeln('1. PI............: ', PIvAL:0:8);
  writeln('2. Número de Euler: ', EULERvAL:0:8);
  writeln('3. Gravidade......: ', GRAVITY:0:5);
  writeln('4. Velocidade Luz.: ', LIGHTsPEED:0:0);
  writeln('5. Razão Áurea....: ', GOLDENrATIO:0:8);
  writeln('6. Número Avogadro: ', AVOGADRO:0:0);
  writeln('7. Constante Planck: ', PLANCK:0:10);
  writeln('8. Carga Elétron..: ', ELECTRONcHARGE:0:10);
  
  writeln;
  writeln('Valores Hexadecimais:');
  writeln('---------------------');
  writeln('9. Máscara de Flags: ', MASKfLAGS);
  writeln('10. Código de Erro..: ', ERRORcODE);
  
  writeln;
  writeln('Operações com Hexadecimais:');
  writeln('--------------------------');
  writeln('MASKfLAGS AND 0x00FF = ', MASKfLAGS and $00FF);
  writeln('ERRORcODE OR 0x0100 = ', ERRORcODE or $0100);
  
  writeln;
  writeln('Pressione ENTER para sair...');
  readln;
end.