using System;
using System.Collections;
using System.Collections.Generic;
public class Program
{
    static void Main(string[] args)
    {
        var dict = Huffman.GetFrequenciesDictionary("internet");
        var initPQ = Huffman.GetInitialPriorityQueue(dict);
        var adjustedQ = Huffman.AdjustPriorityQueue(initPQ);
        var codesDict = Huffman.GetCodes(adjustedQ);
        Console.WriteLine(codesDict.Count);
        foreach (var d in codesDict)
            Console.WriteLine($"{d.Key}: {d.Value}");

        
    }
}

public class HeapNode
{
    public char Data { get; set; }
    public int Frequency { get; set; }
    public HeapNode LeftNode { get; set; }
    public HeapNode RightNode { get; set; }
    public HeapNode(char data, int frequency)
    {
        Data = data;
        Frequency = frequency;
    }
}

public class Huffman
{
    static char defChar = (char)0;

    public static Dictionary<char, int> GetFrequenciesDictionary(string message)
    {
        Dictionary<char, int> dict = new();

        foreach (char c in message)
        {
            if (dict.ContainsKey(c))
            {
                dict[c] += 1;
            }
            else
            {
                dict[c] = 1;
            }
        }
        return dict;
    }

    public static PriorityQueue<HeapNode, int> GetInitialPriorityQueue(Dictionary<char, int> dict)
    {
        PriorityQueue<HeapNode, int> que = new();

        foreach (var d in dict)
        {
            HeapNode heapNode = new(d.Key, d.Value);
            que.Enqueue(heapNode, d.Value);
        }
        return que;
    }

    public static PriorityQueue<HeapNode, int> AdjustPriorityQueue(PriorityQueue<HeapNode, int> q)
    {
        HeapNode top, left, right;
        int newFrequency;

        while (q.Count > 1)
        {
            left = q.Dequeue();
            right = q.Dequeue();
            newFrequency = left.Frequency + right.Frequency;
            top = new HeapNode(defChar, newFrequency);
            top.LeftNode = left;
            top.RightNode = right;
            q.Enqueue(top, newFrequency);
        }
        return q;
    }

    public static Dictionary<char, string> GetCodes(PriorityQueue<HeapNode, int> q)
    {
        Dictionary<char, string> codesDict = new();
        GenerateCodes(codesDict, q.Peek(), "");
        return codesDict;
    }

    private static void GenerateCodes(Dictionary<char, string> codes, HeapNode node, string str)
    {
        if (node == null) return;
        if (node.Data != defChar)
        {
            codes[node.Data] = str;
        }
        GenerateCodes(codes, node.LeftNode, str + "0");
        GenerateCodes(codes, node.RightNode, str + "1");
    }
}