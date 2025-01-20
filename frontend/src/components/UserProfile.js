import React from "react";

function UserProfile() {
    const MEDIA_URL = "http://localhost:8000/media/";
    return (
        <div className="flex flex-col items-center">
            <img
                className="w-16 h-16 mb-2 rounded-full" 
                src={`${MEDIA_URL}img/me.png`}
                alt="me"
            />
            <div className="font-medium dark:text-white text-center">
                <div>John Molina</div>
                <div className="text-sm text-gray-500 dark:text-gray-400">
                    Full-Stack Software Engineer
                </div>
            </div>
        </div>
    );
}

export default UserProfile;
