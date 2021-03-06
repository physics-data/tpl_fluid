#!/usr/bin/env python3

ENABLE_GIF = True

import numpy as np

if ENABLE_GIF:
    from PIL import Image
import utils
import math
import json


def main():
    # TODO: Read parameters from `input.json`
    # width = ?
    # height = ?
    # time = ?
    # viscosity = ?
    # splats = ?

    # Simulator
    sim = Fluid(height, width, viscosity)

    # GIF frames
    frames = []

    for step in range(0, time):
        print("Step: %d" % (step))

        # Create splats in the simulation domain
        for splat in splats:
            if splat["time_from"] <= step and splat["time_to"] > step:
                sim.splat(
                    splat["center"], splat["radius"], splat["accel"], splat["dyes"]
                )

        # Calculate new velocity / dye density after this time slice
        sim.step()

        # Render GIF
        if ENABLE_GIF:
            frames.append(Image.fromarray((sim.dyes * 255).astype("uint8")))
            frames[0].save(
                "output.gif",
                save_all=True,
                append_images=frames[1:],
                duration=30,
                loop=0,
            )

    print("Done!")

    # TODO: Save velocity and dye density field into `output.hdf5`


def grad(f):
    # TODO(Chapter 3.1): implement gradient operator
    raise NotImplementedError


def diverg(f):
    # TODO(Chapter 3.1): implement divergence operator
    raise NotImplementedError


class Fluid:
    def __init__(self, height, width, viscosity):
        self.height = height
        self.width = width

        # Velocity field, self.velocity[:,:,0] is the x-component, self.velocity[:,:,1] is the y-component
        self.velocity = np.zeros((height, width, 2), dtype=np.double)

        # Dye density field. Has a maximum value of 1. Corresponding to RBG colors.
        self.dyes = np.zeros((height, width, 3), dtype=np.double)

        self.viscosity = viscosity

        print("Preparing velocity diffusion solver...")
        # TODO(Chapter 3.3): Instantiate velocity diffusion solver
        # self.diffusion_solver = utils.build_poisson_solver(self.height, self.width, ?, ?, ?)
        print("Preparing pressure solver...")
        # TODO(Chapter 3.4): Instantiate pressure solver
        # self.pressure_solver = utils.build_poisson_solver(self.height, self.width, ?, ?, ?)

    def splat(self, center, r, accel, dyes):
        for dx in range(-r, r + 1):
            for dy in range(-r, r + 1):
                x = center[0] + dx
                y = center[1] + dy

                if x < 0 or x >= self.height or y < 0 or y >= self.width:
                    continue

                if np.linalg.norm([dx, dy]) <= r:
                    self.velocity[x, y] += accel
                    self.dyes[x, y] = np.clip(self.dyes[x, y] + dyes, None, 1)

    def read_field(self, f, i, j):
        ni = np.clip(i, 0, self.height - 1).astype(int)
        nj = np.clip(j, 0, self.width - 1).astype(int)
        return f[ni][nj]

    def bilinear(self, f, x, y):
        # TODO(Chapter 3.2.1): Implement bilinear algorithm
        raise NotImplementedError

    def copy_to_boundary(self, f, factor):
        # TODO(Chapter 3.1.1): Implement copy-to-boundary helper
        raise NotImplementedError

    def step(self):
        # =========
        # Advection
        # =========
        # TODO(Chapter 3.2): Implement advection transformation
        # Notice: Please use self.read_field to read velocity field, which snaps out-of-bound reads to the boundar
        advected_velocity = self.velocity  # Change me
        advected_dyes = self.dyes  # Change me

        self.dyes = advected_dyes

        # Reset dye density field outside the boundary
        self.copy_to_boundary(self.dyes, 0)

        # TODO(Chapter 3.1.1): Ensures boundary conditions for our velocity field
        # self.copy_to_boundary(advected_velocity, ?)

        # ===============
        # Speed diffusion
        # ===============
        # TODO(Chapter 3.3): Implement speed diffusion transformation
        diffused_velocity = advected_velocity  # Change me

        # TODO(Chapter 3.1.1): Ensures boundary conditions for our velocity field
        # self.copy_to_boundary(diffused_velocity, ?)

        # ==========
        # Projection
        # ==========
        # TODO(Chapter 3.4): Implementation projection transformation
        #
        # The outline are as followed:
        # 1. Solve \nabla^2 q = diverg(diffused_velocity) using the pre-constructed solver
        # 2. Ensure q's boundary condition with self.copy_to_boundary
        # 3. Subtract grad(q) from diffused_velocity

        # TODO(Chapter 3.1.1): Ensures boundary conditions for our velocity field one last time
        # self.copy_to_boundary(self.velocity, ?)


if __name__ == "__main__":
    main()
