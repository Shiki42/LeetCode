class Solution {
    public String longestCommonPrefix(String[] strs) {
        String confix = "";
        int lst = 201;
        for(String s : strs) {
            if ( s.length() < lst ) {
                lst = s.length();
            }
        };
        for(int i = 0; i < lst; i++) {
            String nxt = String.valueOf(strs[0].charAt(i));
            int flag = 1;
            for(String s : strs) {
                if( !String.valueOf(s.charAt(i)).equals(nxt)) {
                    flag = 0;
                }
            }
            System.out.println(flag);
            if(flag == 1) {
                confix = confix + nxt;
                System.out.println(confix);
            } else {
                break;
            }
        }

        return confix;
    }
}