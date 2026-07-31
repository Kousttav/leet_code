public String smallestPalindrome(String s) {

    char[] sc = new char[s.length()];

    int p1 = 0;
    int p2 = s.length()-1;

    int[] letters = new int[26];

    for(int i = 0; i<s.length(); i++)
    {
        char c = s.charAt(i);

        letters[c-'a']++;
    }



    Character odd = null;
    for(int i = 0; i<letters.length; i++)
    {
        char c = (char) ('a'+i);
        int side = 0;
        if(letters[i] % 2 == 0)
        {

            side = letters[i] / 2;
            letters[i] = 0;
        }
        else
        {
             side = (letters[i] -1) / 2;
            letters[i] = 1;
           
            odd =c;
        }

         

        for(int j = 0; j<side; j++)
        {
            sc[p1] = c;
            sc[p2] = c;
            p1++;
            p2--;
        }
    }


    if(s.length() % 2 != 0)
        sc[p1] = odd;
     

     return  new String(sc);
}