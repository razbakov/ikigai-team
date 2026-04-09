import React from "react";
import { Composition } from "remotion";
import { IkigaiVideo, totalDuration } from "./IkigaiVideo";

export const RemotionRoot: React.FC = () => {
  return (
    <>
      <Composition
        id="IkigaiTeam"
        component={IkigaiVideo}
        durationInFrames={totalDuration}
        fps={30}
        width={1280}
        height={720}
      />
    </>
  );
};
