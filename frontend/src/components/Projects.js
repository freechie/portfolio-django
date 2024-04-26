import React, { useEffect, useState } from 'react';
import axios from 'axios';
import { capitalize } from '../utils/utils';
import { LoadingAnimation } from '../utils/utils';

const Projects = () => {
    const [projects, setProjects] = useState([]);
    const [isLoading, setIsLoading] = useState(true);

    useEffect(() => {
        const fetchProjects = async () => {
            setIsLoading(true);
            try {
                const response = await axios.get('http://localhost:8000/api/projects/');
                setProjects(response.data);
            } catch (error) {
                console.error('There was an error fetching the projects:', error);
            } finally {
                setIsLoading(false);
            }
        };

        fetchProjects();
    }, []);

    const handleProjectClick = (project) => {
        window.location.href = `/project/${project.id}/`;
    };

    return (
        <div className='flex flex-col items-center w-full min-h-screen bg-gray-50 dark:bg-gray-900 text-gray-900 dark:text-white'>
            <h1 className='text-3xl font-bold py-8'>My Projects</h1>
            {isLoading ? (
                <LoadingAnimation />
            ) : projects.length > 0 ? (
                <div className='flex overflow-x-auto pb-4'>
                    <div className='flex flex-nowrap lg:ml-40 md:ml-20 ml-10'>
                        {projects.map((project) => (
                            <div
                                key={project.id}
                                className='inline-block px-3 w-48 h-64 m-2 bg-white dark:bg-gray-800 rounded-lg shadow cursor-pointer hover:shadow-lg transition-shadow duration-300'
                                onClick={() => handleProjectClick(project)}
                            >
                                <h2 className='text-lg font-semibold mb-1 text-center'>
                                    {capitalize(project.title)}
                                </h2>
                                {project.images && project.images.length > 0 && (
                                    <img
                                        src={project.images[0].image}
                                        alt={project.images[0].caption || 'Project thumbnail'}
                                        className='w-full h-32 object-cover rounded mb-1'
                                    />
                                )}
                            </div>
                        ))}
                    </div>
                </div>
            ) : (
                <p className='text-lg'>No projects found.</p>
            )}
        </div>
    );
};

export default Projects;
