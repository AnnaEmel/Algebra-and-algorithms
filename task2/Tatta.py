
# coding: utf-8

# In[ ]:

import math

class Graph:
    v = {}
    e = set()

    _forces = {}
    _velocities = {}

    def reset(self, num_verts):
        for i in range(num_verts):
            self.v[i+1] = (i*2, i*2, False) # x, y, pinned

    def load(self, filename):
        f = open(filename, 'r')

        if not f:
            return

        l = f.readline()
        num_v_e = l.split()
        self.reset(int(num_v_e[0]))

        l = f.readline()
        fixed_ones = l.split()
        counter = 0
        for i_str in fixed_ones:

            i = int(i_str)
            x = 0
            y = 0

            if counter >= 1:
                x = 1

            if counter == 2:
                y = 1
            
            self.v[i] = (x, y, True)
            
            counter += 1

        for i in range(int(num_v_e[1])):
            l = f.readline()
            source_target = l.split()
            self.connect(int(source_target[0]), int(source_target[1]))
        
        f.close()

    def read_stdin(self):
        l = input()
        num_v_e = l.split()
        self.reset(int(num_v_e[0]))

        l = input()
        fixed_ones = l.split()
        counter = 0
        for i_str in fixed_ones:

            i = int(i_str)
            x = 0
            y = 0

            if counter >= 1:
                x = 1

            if counter == 2:
                y = 1
            
            self.v[i] = (x, y, True)
            
            counter += 1

        for i in range(int(num_v_e[1])):
            l = input()
            source_target = l.split()
            self.connect(int(source_target[0]), int(source_target[1]))

    def connect(self, vert1, vert2):
        self.e.add((vert1, vert2))

    def save_GEFX(self, name):
        if not '.gexf' in name:
            name += '.gexf'
            
        f = open(name, 'w')
        if not f:
            return

        f.write('<?xml version="1.0" encoding="UTF-8"?><gexf xmlns="http://www.gexf.net/1.3" version="1.3" xmlns:viz="http://www.gexf.net/1.3/viz" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://www.gexf.net/1.3 http://www.gexf.net/1.3/gexf.xsd"><meta lastmodifieddate="2017-01-07"><creator>Gephi 0.9</creator><description></description></meta><graph defaultedgetype="directed" mode="static"><nodes>')

        for v_id in self.v:
            f.write('<node id="' + str(v_id) + '" label="0">')
            f.write('<viz:size value="3.0"></viz:size>')
            f.write('<viz:position x="' + str(self.v[v_id][0]*100) + '" y="' + str(self.v[v_id][1] * 100) + '"></viz:position>')
            f.write('</node>')

        f.write('</nodes>')
        f.write('<edges>')
        
        edge_counter = 0
        for e in self.e:
            f.write('<edge id="' + str(edge_counter) + '" source="' + str(e[0]) + '" target = "' + str(e[1]) + '"></edge>')
            edge_counter += 1
            
        f.write('</edges>')
        f.write('</graph></gexf>')
        
        f.close()

    def save(self, name):
        if not '.txt' in name:
            name += '.txt'

        f = open(name, 'w')
        if not f:
            return

        f.write(str(self))

        f.close()

    def __str__(self):
        string = ''
        for v in self.v:
            vert = self.v[v]
            string += str(vert[0]) + ' ' + str(vert[1]) + '\n'

        string = string[:-1]

        return string
    
    def deploy(self):
        max_num_steps = 1000000000
        stop_sim = False
        
        self._velocities = {}
        steps_count = 0

        while self.sim_step(): #and steps_count < max_num_steps:
            steps_count += 1


    def sim_step(self):
        k = 0.001
        vel_treshold = 0.000001
        en_loss = 0.9
        
        stop_sim = True
        self._forces = {}
        for e in self.e:
            source = self.v[e[0]]
            target = self.v[e[1]]

            dx = target[0] - source[0]
            dy = target[1] - source[1]


            d2 = dx*dx + dy*dy
            nx = 0
            ny = 0
            if d2 > 0.01:
                nx = dx / math.sqrt(d2)
                ny = dy / math.sqrt(d2)

            f = k*d2

            if not e[0] in self._forces:
                self._forces[e[0]] = (0.0, 0.0)

            if not e[1] in self._forces:
                self._forces[e[1]] = (0.0, 0.0)

            self._forces[e[0]] = (self._forces[e[0]][0] + nx*f, self._forces[e[0]][1] + ny*f)
            self._forces[e[1]] = (self._forces[e[1]][0] - nx*f, self._forces[e[1]][1] - ny*f)


        for v in list(self.v.keys()):
            if not v in self._velocities:
                self._velocities[v] = (0.0, 0.0)
            if not v in self._forces:
                continue
                
            vert = self.v[v]
            if not vert[2]: # if not pinned
                new_vel = (self._velocities[v][0] + self._forces[v][0], self._velocities[v][1] + self._forces[v][1])
                vel_val = new_vel[0]*new_vel[0] + new_vel[1]*new_vel[1]
                if vel_val > vel_treshold:
                    stop_sim = False

                new_vel = (new_vel[0]*en_loss, new_vel[1]*en_loss)
                self._velocities[v] = new_vel
                self.v[v] = (vert[0] + new_vel[0], vert[1] + new_vel[1], vert[2])

        return not stop_sim

graph = Graph()
graph.read_stdin()
graph.load()
graph.deploy()
print(graph)

