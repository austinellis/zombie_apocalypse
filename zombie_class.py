class ZombieApoc():

    def __init__(self):
        # Current population as of Nov. 22, 2014
        self.population = 7276206460

        # Percent of population who are immune
        self.immune_perc = .01

        # Time until infected person shows symptons
        self.time_dormant = 360

        # Time until infected person becomes a zombie in minutes and
        # can infect others
        self.time_to_change = 60

        # How long does a zombie live in days
        self.lifespan = 100

        # How many people each zombie infects per day
        self.number_infect_day = 6

    def CustomApoc(self, population1, immune_perc1, time_dormant1,
                   time_to_change1, lifespan1, number_infect_day1):
        """Modify all 6 variables: population, immune percent, time dormant,
        time to change, life span, number infected
        """
        self.population = population1
        self.immune_perc = immune_perc1
        self.time_dormant = time_dormant1
        self.time_to_change = time_to_change1
        self.lifespan = lifespan1
        self. number_infect_day = number_infect_day1

    def ChangePop(self, population1):
        """Use a custom population variable
        """
        self.population = population1

    def ChangeImmunePer(self, immune_perc1):
        """Use a custom immune percentage variable
        """
        self.immune_perc = immune_perc1

    def ChangeTimeDormant(self, time_dormant1):
        """Use a custom dormant time variable
        """
        self.time_dormant = time_dormant1

    def ChangeTimeToChange(self, time_to_change1):
        """Use a custom time to change variable
        """
        self.time_to_change = time_to_change1

    def ChangeLifespan(self, lifespan1):
        """Use a custom lifespan variable
        """
        self.lifespan = lifespan1

    def ChangeNumberInfectDay(self, number_infect_day1):
        """Use a custom number infected per day by each zombie variable
        """
        self.number_infect_day = number_infect_day1

    def CalcApoc(self):
        days = 0
        infected = 1
        possible_infected = self.population * (1 - self.immune_perc)
        # print 'Possible Infected: ' + str(possible_infected)
        while infected < possible_infected:
            print 'Day: ' + str(days)
            print 'Infected: ' + format(infected, ',')
            infected += infected * self.number_infect_day
            days += 1
            print 'Possible infected: ' + format(possible_infected, ',')
            #print 'Infected: ' + format(infected, ',')
        #print 'Infected: ' + format(infected, ',')
        return days

    def __str__(self):
        printStr = 'Population: ' + str(self.population) + '\n' \
            'Immune: ' + str(self.immune_perc) + '\n' \
            'Dormant: ' + str(self.time_dormant) + '\n' \
            'Time to change: ' + str(self.time_to_change) + '\n' \
            'Life Span: ' + str(self.lifespan) + '\n' \
            'Number infected per day: ' + str(self.number_infect_day)
        return printStr


def test():
    zombie = ZombieApoc()
    # print zombie
    days_survived = zombie.CalcApoc()
    # print '\n\n'
    #print zombie, '\n'
    print days_survived


def testChange():
    zombie = ZombieApoc()
    print zombie, '\n'
    zombie.ChangePop(100000)
    zombie.ChangeImmunePer(.1)
    zombie.ChangeTimeDormant(48)
    zombie.ChangeTimeToChange(30)
    zombie.ChangeLifespan(30)
    zombie.ChangeNumberInfectDay(1)
    print zombie
