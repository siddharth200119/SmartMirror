import React, { useState } from 'react';

function Webcam() {

    const [playing, setPlaying] = useState(false);
    const HEIGHT = 500;
    const WIDTH = 500;

    const startVideo = () => {
        setPlaying(true)
        navigator.getUserMedia(
            {video: true,},
            (stream) => {
                let video = document.getElementsByClassName("videofeed")[0];
                if (video){
                    video.srcObject = stream
                }
            },
            (err) => console.log(err)
        );
    };

    const stopVideo = () => {
        setPlaying(false)
        let video = document.getElementsByClassName("videofeed")[0];
        video.srcObject.getTracks()[0].stop();
    };   

    return (
        <div>
            <div className='videofeed_container'>
                <video
                    height={HEIGHT}
                    width={WIDTH}
                    muted
                    autoPlay
                    className='videofeed'
                ></video>
                <div>
                    {playing? (
                        <button onClick={stopVideo}>Stop</button>
                    ) : (
                        <button onClick={startVideo}>Start</button>
                    )}
                </div>
            </div>
        </div>
    );
}

export default Webcam;
