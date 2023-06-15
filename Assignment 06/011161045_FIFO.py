import numpy as np

np.random.seed(10)


class SSQ:
    def __init__(self):

        self.inter_arrivals = list(np.abs(np.random.normal(loc=2, scale=1, size=100)))
        self.service_times = list(np.random.uniform(low=3, high=4, size=100))

        print(self.inter_arrivals)
        print(self.service_times)

        self.clock = 0.00

        self.next_arrival = self.inter_arrivals.pop(0)
        self.next_departure = float('inf')

        self.num_in_queue = 0
        self.times_of_arrival_in_queue = []
        self.service_times_in_queue = []

        self.total_delay = 0.00
        self.num_of_delays = 0.00

        self.server_status = 0
        self.last_event_time = 0.00

        self.total_idle_time = 0.00
        self.idle_start_time = 0.00

        self.customer_num_in_queue_start = 0.00
        self.customer_num_duration_in_queue = []

    def arrival(self):
        self.next_arrival += self.inter_arrivals.pop(0)

        if self.server_status == 0:
            self.server_status = 1
            self.total_idle_time += (self.clock - self.idle_start_time)
            delay = 0.00
            self.total_delay += delay
            self.num_of_delays += 1
            self.next_departure = self.clock + self.service_times.pop(0)

        else:
            self.num_in_queue += 1
            duration = self.clock - self.customer_num_in_queue_start

            if len(self.customer_num_duration_in_queue) == len(self.times_of_arrival_in_queue):
                self.customer_num_duration_in_queue.append(duration)
            else:
                self.customer_num_duration_in_queue[len(self.times_of_arrival_in_queue)] += duration

            self.times_of_arrival_in_queue.append(self.clock)
            self.customer_num_in_queue_start = self.clock

            self.service_times_in_queue.append(self.service_times.pop(0))

    def departure(self):
        if self.num_in_queue == 0:
            self.server_status = 0
            self.idle_start_time = self.clock
            self.next_departure = float('inf')
        else:
            self.num_in_queue -= 1
            arrival = self.times_of_arrival_in_queue.pop(0)  # FIFO
            delay = self.clock - arrival
            self.total_delay += delay
            self.num_of_delays += 1

            self.next_departure = self.clock + self.service_times_in_queue.pop(0)

    def simulate_next_event(self):
        self.clock = min(self.next_arrival, self.next_departure)
        self.last_event_time = self.clock

        if self.next_arrival <= self.next_departure:
            self.arrival()
            print("arrival at -> " + str(self.clock))

        else:
            self.departure()
            print("departure at -> " + str(self.clock))

        print("Server status: ", self.server_status)
        print("Times of arrival in the queue: ", self.times_of_arrival_in_queue)
        print("Service times in the queue: ", self.service_times_in_queue)
        print("Total delay: ", self.total_delay)
        print("Next arrival : ", self.next_arrival)
        print("Next departure: ", self.next_departure)

    def start(self):
        while self.num_of_delays < 10:
            self.simulate_next_event()
        print("------------------------------------------------result-------------------------------------------------")
        print(f'Average delay: {self.total_delay / 50}')
        result = 0
        for i in range(1, len(self.customer_num_duration_in_queue)):
            result += (i * self.customer_num_duration_in_queue[i])

        print(f'Expected number of customer in the queue: {result / self.last_event_time}')
        print(f'Expected utilization of the server: '
              f'{(self.last_event_time - self.total_idle_time) / self.last_event_time}')


s = SSQ()
s.start()
