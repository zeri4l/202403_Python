class Main {
    public static void main(String[] args) {
        int num[] = {2, 1, 4, 5, 6, 3};
        int numb[] = new int[10];

        for (int i = 0; i < num.length; i++) {
            numb[i] = num[i];
        }

        for (int i : numb) {
            System.out.print(i + " ");
        }
    }
}