using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace App
{
    class Program
    {
        static void Main(string[] args)
        {
            //Console.Write("Please write a your first name:");
            //String String1 = Console.ReadLine();
            //Console.Write("Please click Enter");
            //String String2 = Console.ReadLine();
            //Console.WriteLine(String1 + String2);
            Console.Write("Please write a number:");
            int int1 = int.Parse(Console.ReadLine());
            Console.Write("Please write the second number:");
            int int2 = int.Parse(Console.ReadLine());
            Console.WriteLine(summer(int1, int2));
            Console.WriteLine(int1 - int2);
            Console.WriteLine(int1 * int2);
            if (int2 == 0)
                Console.WriteLine("Division is impossible!");
            else
                Console.WriteLine(int1 / int2);
            Console.ReadKey();
        }
        static int summer(int int1, int int2)
        {
            return int1 + int2;

        }
    }
}
