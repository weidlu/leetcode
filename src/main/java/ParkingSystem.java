/**
 * leetcode 1603
 */
public class ParkingSystem {

    int[] park = new int[3];

    public ParkingSystem(int big, int medium, int small) {
        park[0] = big;
        park[1] = medium;
        park[2] = small;
    }

    public boolean addCar(int carType) {
        int index = --carType;
        return --park[index] >= 0;
    }

}
