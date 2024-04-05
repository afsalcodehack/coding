package com.company;

public class Main {

    public static void main(String[] args) {
        int n  = 10;

        int i = 1;
        
        int count = 0;

        for (String e : new String[]{"Volvo", "BMW", "Ford", "Mazda"}){
            System.out.println(e);
        }


        System.out.println("hello this is my code");
        
        while( n > count)
        {
           if( i % 2 == 0)
           {
                System.out.println(i);
                count++;
           }
            i++;
        }
    }
}
