# [백준 1062](https://www.acmicpc.net/problem/1062)

import java.io.FileInputStream;
import java.util.Arrays;
import java.util.Scanner;

public class baekjoon {
    static int N, K;
    static boolean[] visited;
    static String[] words;
    static int selectedCount = 0;
    static int max = 0;

    public static void main(String[] args) throws Exception {
        System.setIn(new FileInputStream("src\\input.txt"));
        Scanner sc = new Scanner(System.in);

        N = Integer.parseInt(sc.next());
        K = Integer.parseInt(sc.next());

        words = new String[N];
        visited = new boolean[26];

        // a, b, t, i, c
        visited['a' - 'a'] = true; // visitied[0]=true
        visited['n' - 'a'] = true; // visitied[13]=true
        visited['t' - 'a'] = true; // visitied[19]=true
        visited['i' - 'a'] = true;
        visited['c' - 'a'] = true;

        selectedCount = 5; // 소문자 종류

        //words 입력

        // 앞쪽의 antic 잘라내기
        for (int i = 0; i < N; i++) {
            words[i] = sc.next().replaceAll("[antic]", "");
        }

        // 문자의 종류가 5보다 작으면 종료
        if (K < 5) {
            System.out.println(0);
            return;
        }

        max = countWords();

        for (int i = 0; i < 26; i++) {
            if (!visited[i]) {
                dfs(i);
            }
        }

        // max 출력
        System.out.println(max);
    }

    static void dfs(int index) {

        //1.체크인 => visited[index] = true, selectedCount
        visited[index] = true;
        selectedCount++;

        //2.목적지인가? => selectedCount 가 K에 도달했는가? -> max 갱신
        if (selectedCount == K) {
            max = Math.max(countWords(), max);
        } else {
            //3.연결된 곳을 순회 => index + 1 ~ 26
            for (int i = index + 1; i < 26; i++) {

                //4.갈 수 있는가? => visited[next] == false
                if (!visited[i]) {
                    //5.간다 => dfs(next)
                    dfs(i);
                }
            }
        }

        //6. 체크아웃 => visited[index] = false, selectedCount
        visited[index] = false;
        selectedCount--;

    }

    // N개의 단어 중 읽을 수 있는 단어 개수
    static int countWords() {
        int count = 0;
        for (int i = 0; i < N; i++) {

            String word = words[i];
            boolean isPossible = true;

            for (int j = 0; j < word.length(); j++) {

                if (visited[word.charAt(j) - 'a'] == false) {
                    isPossible = false;
                    break;
                }
            }

            if (isPossible) {
                count++;
            }
        }
        return count;
    }
}
