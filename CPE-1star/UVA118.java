import java.util.Scanner;

public class UVA118 {
    public static String direction(String instruction, String side) {
        if (side.equals("E")) {
            if (instruction.equals("R")) {
                return "S";
            } else if (instruction.equals("L")) {
                return "N";
            }
        } else if (side.equals("W")) {
            if (instruction.equals("R")) {
                return "N";
            } else if (instruction.equals("L")) {
                return "S";
            }
        } else if (side.equals("N")) {
            if (instruction.equals("R")) {
                return "E";
            } else if (instruction.equals("L")) {
                return "W";
            }
        } else if (side.equals("S")) {
            if (instruction.equals("R")) {
                return "W";
            } else if (instruction.equals("L")) {
                return "E";
            }
        }
        return "";
    }
    Scanner sc = new Scanner(System.in);
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        while (true) {
            try {
                int x = scanner.nextInt();
                int y = scanner.nextInt();
                int[][] world = new int[y + 1][x + 1];

                while (true) {
                    int initialX = scanner.nextInt();
                    int initialY = scanner.nextInt();
                    String side = scanner.next();
                    String instructions = scanner.next();

                    int subX = 0;
                    int subY = 0;
                    int check = 0;
                    String subside = "";

                    for (int i = 0; i < instructions.length(); i++) {
                        char instruction = instructions.charAt(i);
                        if (instruction != ' ') {
                            subside = side;
                            subX = initialX;
                            subY = initialY;

                            if (instruction == 'R' || instruction == 'L') {
                                side = direction(Character.toString(instruction), side);
                            } else {
                                if (side.equals("E")) {
                                    initialX++;
                                } else if (side.equals("W")) {
                                    initialX--;
                                } else if (side.equals("N")) {
                                    initialY++;
                                } else if (side.equals("S")) {
                                    initialY--;
                                }

                                if (initialX > x || initialX < 0 || initialY > y || initialY < 0) {
                                    if (world[subY][subX] != 0) {
                                        world[subY][subX] = 0;
                                        check = 1;
                                        break;
                                    } else {
                                        initialX = subX;
                                        initialY = subY;
                                    }
                                }
                            }
                            System.out.println(subX + " " + subY);
                        }
                    }

                    if (check == 1) {
                        System.out.println(subX + " " + subY + " " + subside + " LOST");
                    } else {
                        System.out.println(initialX + " " + initialY + " " + side);
                    }
                }
            } catch (Exception e) {
                break;
            }
        }
        scanner.close();
    }
}