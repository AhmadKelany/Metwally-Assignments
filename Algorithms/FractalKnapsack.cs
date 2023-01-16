using System;
using System.Linq;
using System.Collections.Generic;
public class Program
{
    public record Item(int Id,decimal Profit,decimal Weight);
    public static void Main()
    {
        List<Item> items = new List<Item>() {new Item(0,4,1) ,new Item(1,9,2) ,new Item(2,12,10),new Item(3,11,4),new Item(4,6,3),new Item(5,5,5)};
        var result = GetItemsWithMaxProfit(items,12);
        foreach(var r in result )
        {
            Console.WriteLine($"id: {r.Id}, weight= {r.Weight:N2}, profit= {r.Profit:N2}");
        }
        Console.WriteLine($"Total profit= {result.Sum(t => t.Profit):N2}");
    }
    public static List<Item> GetItemsWithMaxProfit(List<Item> items, decimal maxWeight)
    {
        List<Item> result = new();
        items = items.OrderByDescending(i => i.Profit/i.Weight).ToList();
        int i = 0;
        while(maxWeight > 0)
        {
            int id = items[i].Id;
            decimal weight = items[i].Weight >= maxWeight ? maxWeight : items[i].Weight;
            decimal profit = weight * items[i].Profit / items[i].Weight;
            result.Add(new Item(id,profit,weight));
            maxWeight -= weight;
            i++; 
        }
        return result;
    }
}