using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace WpfApplication2
{
    class Food
    {
        public string Name{get; set;}
        public decimal Price{get; set;}
        public string Description{get; set;}
        public int Calories{get; set;}

        public override string ToString()
        {

            return string.Format("Name: {0} \r\n Description: {1} \r\n Price: ${2} \r\n Calories: {3}", this.Name, this.Description, this.Price, this.Calories);
        }
    }
}

