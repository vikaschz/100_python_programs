"""
Create an abstract class Robot with perform_task(). Implement CleaningRobot, SecurityRobot, DeliveryRobot.
"""

from abc import ABC, abstractmethod


class Robot(ABC):

    @abstractmethod
    def perform_task(self):
        pass


class CleaningRobot(Robot):

    def perform_task(self):
        print("Cleaning Robot Activated..")


class SecurityRobot(Robot):
    def perform_task(self):
        print("Security Robot Activated..")


class DeliveryRobot(Robot):
    def perform_task(self):
        print("Delivery Robot Activated..")


robots = [CleaningRobot(), SecurityRobot(), DeliveryRobot()]

for robot in robots:
    robot.perform_task()

