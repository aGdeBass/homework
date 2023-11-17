using System.Globalization;


string test = @"2 3
1 2 3
4 5 6"

Console.SetIn( new StringReader(test1));
int [] wymiary = Array.ConvertAll(Console.ReadLine().Split(" "), int.Parse);
var n = wymiary[0]; // wierszy
var m = wymiary[1]; // kolumne

int [,] a = new int[n,m];

for (int i = 0; i < n; i++)
{
    //czytaj i-ty wiersz

    var wiersz = Array.ConvertAll(Console.ReadLine().Split(" "), int.Parse);

    //wypełnij tablice a wczytamy dane
    for (int j = 0 ; j < m; j++)
    {
        a[i,j] = wiersz[j];
    }
} 


PrintMatrixTranspored(a);

void PrintMatrix(int[,] matrix)
{
    for (int wiersz = 0; wiersz < matrix.GetLength(0); wiersz++)
    {
        for (int kolumna = 0; kolumna < matrix.GetLength(1); kolumna++)
        {
            Console.Write(matrix[wiersz, kolumna] + " ");
        }
        Console.WriteLine();
    }
}

void PrintMatrixTranspored(int[,] matrix)
{
    for (int kolumna = 0; kolumna < matrix.GetLength(1); kolumna++)
    {
        for (int wiersz = 0; wiersz < matrix.GetLength(0); wiersz++)
        {
            Console.Write(matrix[kolumna, wiersz] + " ");
        }
        Console.WriteLine();
    }
}