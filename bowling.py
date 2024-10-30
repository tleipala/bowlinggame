from bowling_error import BowlingError
from frame import Frame

class BowlingGame:

    def __init__(self):
        self._frames = []


    def add_frame(self, frame: Frame) -> None:
        if len(self._frames) == 10:
            raise BowlingError
        self._frames.append(frame)

    def get_frame_at(self, i: int) -> Frame:
        if i >= len(self._frames):
            raise BowlingError
        return self._frames[i]

    def calculate_score(self) -> int:
        score = 0
       # is_spare = False
        #is_strike = False
        for i,frame in enumerate(self._frames):
            if frame.is_spare():
                if i == len(self._frames)-1:
                    frame.set_bonus(self._bonus_throw)
                else:
                    frame.set_bonus(self._frames[i+1].get_first_throw())
               # is_spare = True
            if frame.is_strike():
                if i == len(self._frames)-1:
                    frame.set_bonus(self._bonus_throw + self._second_bonus_throw)
                else:
                    if i == len(self._frames)-2:
                        if self._frames[i + 1].is_strike():
                            frame.set_bonus(
                                self._frames[i+1].get_first_throw() + self._frames[i+1].get_second_throw() +
                                self._bonus_throw)
                        else:
                            frame.set_bonus(self._frames[i+1].get_first_throw()+self._frames[i+1].get_second_throw())
                    elif self._frames[i + 1].is_strike():
                                frame.set._bonus(self._frames[i + 1].get_first_throw() + self._frames[i + 1].get_second_throw() +
                                self._frames[i + 2].get_first_throw())
                    else:
                        frame.set_bonus(self._frames[i + 1].get_first_throw() + self._frames[i + 1].get_second_throw())
                #is_strike = True
            score = score + frame.score()
        return score

    def set_first_bonus_throw(self, bonus_throw: int) -> None:
        self._bonus_throw = bonus_throw

    def set_second_bonus_throw(self, bonus_throw: int) -> None:
        self._second_bonus_throw = bonus_throw

            # if is_strike:
            #    score = score + frame.get_first_throw()+ frame.get_second_throw()
            #   if frame.is_strike():
            #       score = score + self._frames[i+1].get_first_throw()
            #   is_strike = False
            #  if is_spare:
            #    score = score + frame.get_first_throw()
            #    is_spare = False



    #frame.set_bonus(self._frames[i + 1].get_first_throw() + self._frames[i + 1].get_second_throw() + self._frames[
      #  i + 1].get_first_throw() + self._frames[i + 2].get_second_throw())

