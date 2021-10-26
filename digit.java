class day2{//digit print one by one
    public static void main(String args[]){
        Scanner sc= new Scanner(System.in);
        System.out.println("Enter Number: ");
        int num= sc.nextInt();
        
        int nod=0;
        int temp= num;
        while(temp !=0){
            temp=temp/10;
            nod++;
        }
        int div = (int)Math.pow(10,nod -1);
        while(div !=0){
            int q= num/div;
            System.out.println(q);
            num= num% div;
            div = div / 10 ;

        }

    }
}
