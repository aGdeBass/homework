using System.ComponentModel.Design.Serialization;
using System.Dynamic;
using System.Formats.Asn1;
/// <summary>
/// Oblicza obwód trójkąta dowolnego dla zadanych długości boków, zaokrąglając wynik do podanej liczby cyfr po przecinku
/// </summary>
/// <param name="a">długość pierwszego boku, liczba całkowita nieujemna</param>
/// <param name="b">długość drugiego boku, liczba całkowita nieujemna</param>
/// <param name="c">długość trzeciego boku, liczba całkowita nieujemna</param>
/// <param name="precision">dokładność obliczeń (zaokrąglenie), liczba cyfr po przecinku (od 2 do 8)</param>
/// <returns>obwód trójkąta obliczony z zadaną dokładnością</returns>
/// <exception cref="ArgumentOutOfRangeException">z komunikatem "wrong arguments", 
///     gdy <c>precision</c> jest poza przedziałem od 2 do 8 lub którakolwiek z długości jest ujemna</exception>    
/// <exception cref="ArgumentException">z komunikatem "object not exist", gdy trójkąta nie można utworzyć</exception>
/// <remarks>dopuszczamy trójkąt o pokrywających się bokach lub o wszystkich bokach o długości 0</remarks>
/// 



static double TrianglePerimeter(int a, int b, int c, int precision=2)
{
    if(a < 0 || b < 0 || c < 0) throw new ArgumentException("wrong arguments");
    if(a + b < c || b + c < a || c + a < b ) throw new ArgumentException("wrong arguments");
    if(precision < 2 || precision > 8) throw new ArgumentException("object not exist");

    var area = a + b + c;
    return area;
}