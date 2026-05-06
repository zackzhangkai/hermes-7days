import React from 'react';

export const metadata = {
  title: 'Forum',
  description: 'Discussion forum categories',
};

export default function ForumPage() {
  return (
    <section className="max-w-4xl mx-auto py-8">
      <h1 className="text-3xl font-bold mb-6">Forum Categories</h1>
      <p className="mb-4">Browse discussion categories.</p>
      {/* Placeholder list of categories */}
      <ul className="list-disc pl-5 space-y-2">
        <li>General AI Development</li>
        <li>Prompt Engineering</li>
        <li>Tooling & Infrastructure</li>
        <li>Showcase Projects</li>
      </ul>
    </section>
  );
}
