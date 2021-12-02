# day 12

from dataclasses import dataclass


@dataclass
class Moon:
    x: int
    y: int
    z: int
    x_vel: int = 0
    y_vel: int = 0
    z_vel: int = 0

    def potential_energy(self) -> int:
        return abs(self.x)+abs(self.y)+abs(self.z)

    def kinetic_energy(self) -> int:
        return abs(self.x_vel)+abs(self.y_vel)+abs(self.z_vel)

    def total_energy(self) -> int:
        return self.potential_energy()*self.kinetic_energy()

    def update_velocity(self, moons: list) -> None:
        for moon in moons:
            if self.x > moon.x:
                self.x_vel -= 1
            elif self.x < moon.x:
                self.x_vel += 1
            if self.y > moon.y:
                self.y_vel -= 1
            elif self.y < moon.y:
                self.y_vel += 1
            if self.z > moon.z:
                self.z_vel -= 1
            elif self.z < moon.z:
                self.z_vel += 1

    def update_position(self) -> None:
        self.x += self.x_vel
        self.y += self.y_vel
        self.z += self.z_vel


if __name__ == '__main__':
    # sample data 1
    m1 = Moon(-1, 0, 2)
    m2 = Moon(2, -10, -7)
    m3 = Moon(4, -8, 8)
    m4 = Moon(3, 5, -1)
    # sample data 2
    m1 = Moon(-8, -10, 0)
    m2 = Moon(5, 5, 10)
    m3 = Moon(2, -7, 3)
    m4 = Moon(9, -8, -3)
    # my input
    m1 = Moon(-6, -5, -8)
    m2 = Moon(0, -3, -13)
    m3 = Moon(-15, 10, -11)
    m4 = Moon(-3, -8, 3)

    def tick(n: int = 1):
        for i in range(n):
            m1.update_velocity([m2, m3, m4])
            m2.update_velocity([m1, m3, m4])
            m3.update_velocity([m1, m2, m4])
            m4.update_velocity([m1, m2, m3])
            m1.update_position()
            m2.update_position()
            m3.update_position()
            m4.update_position()
            # print(m1,m2,m3,m4)

    def system_energy(moons: list) -> int:
        return sum(map(lambda x: x.total_energy(), moons))

    tick(1000)
    print(system_energy([m1, m2, m3, m4]))
