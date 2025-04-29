public class Main{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int t = sc.nextInt();
        while(t-- != 0){
            int n = sc.nextInt();
            int[] a = new int[n+1];
            int[] b = new int[0];
            a[0] = Integer.MIN_VALUE;   
            for(int i = 1; i < n+1 ;i++){
                a[i] = sc.nextInt();
            }
            b[0] = sc.nextInt();
            boolean ans = false;
            for(int i = 1 ; i < n ; i++){
                if(a[i] > a[i+1]){
                    if(a[i] > b[0] - a[i] && b[0] - a[i] >= a[i-1]){
                        a[i] = b[0] - a[i];
                        if(a[i] > a[i+1]){
                            if(a[i+1] < b[0] - a[i+1]){
                                a[i+1] = b[0] - a[i+1];
                                if(a[i] > a[i+1]){
                                    System.out.println("NO");
                                    ans = true;
                                }
                            }else{
                                System.out.println("NO");
                                ans = true;
                            }
                        }
                    }else{
                        if(a[i+1] < b[0] - a[i+1]){
                            a[i+1] = b[0] - a[i+1];
                                if(a[i] > a[i+1]){
                                    System.out.println("NO");
                                    ans = true;
                                }
                        }else{
                            System.out.println("NO");
                            ans = true;
                        }
                    }
                }
            }
            if(!ans){
                System.out.println("YES");
            }
        }
    }
}